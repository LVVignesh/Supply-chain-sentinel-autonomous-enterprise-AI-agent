# --------------------------------------------------------------------------------------
# THE SUPPLY CHAIN SENTINEL: AUTONOMOUS ENTERPRISE RISK AGENT
# Capstone Project for the Google/Kaggle AI Agents Intensive
# 
# This file contains the consolidated Multi-Agent System architecture, Smart Mock Logic, 
# Tools, and the Gradio dashboard, allowing the project to be run easily in a single file.
# --------------------------------------------------------------------------------------

import os
import time
import json
import gradio as gr
from typing import List, Dict, Any

# --- SMART MOCK DATA GENERATION ---
# Create a temporary JSON file to simulate an internal database/Master Control Program (MCP)
inventory_data = {
    "US_East_Coast": {
        "warehouse_id": "WH-ATL-01",
        "stock": ["Microchips", "Medical Supplies"],
        "capacity": "85%"
    },
    "Hamburg_Port": {
        "warehouse_id": "WH-HAM-99",
        "stock": ["Automotive Parts", "Steel"],
        "capacity": "40%"
    },
    "Shenzhen_Port": {
        "warehouse_id": "WH-SZN-22",
        "stock": ["Lithium Batteries", "Screens"],
        "capacity": "95%"
    }
}
with open("inventory.json", "w") as f:
    json.dump(inventory_data, f, indent=4)

# --- SMART MOCK AGENT FRAMEWORK ---
# ADK's Agent class is mocked to ensure the demo runs without installing the external library.
class Agent:
    """Mock Agent class to simulate ADK behavior and provide deterministic demo output."""
    def __init__(self, name, model="gemini-2.5-flash", instructions=None, tools=None, memory=None):
        self.name = name
        self.instructions = instructions
        self.tools = tools or []
        
    def run(self, query):
        """Simulates the agent's complex reasoning and tool usage."""
        # --- SMART MOCK LOGIC ---
        if self.name == "Watchtower":
            # Scenario: Hamburg Strike (RISK_ALERT)
            if "Hamburg" in query or "Strike" in query:
                return "ALERT: Labor Strike in Hamburg Port affecting Automotive Parts."
            # Scenario: Florida Hurricane (RISK_ALERT)
            if "Florida" in query or "Hurricane" in query:
                return "ALERT: Severe Weather (Storm Gamma) in Florida affecting Electronics."
            # Scenario: Tokyo Earthquake (CLEAR: No Stock)
            if "Tokyo" in query:
                return "CLEAR: No impact (No active inventory in region)."
            # Scenario: Irrelevant News (CLEAR)
            return "CLEAR: No impact."
            
        elif self.name == "Strategist":
            # Strategist recalls the best plan based on the alert context
            if "Florida" in query:
                # Memory Recall: Found plan for past hurricane
                return "Plan: 1. Activate flood barriers at warehouse. 2. Accelerate outgoing shipments. 3. Divert inbound trucks to Georgia."
            # Default plan for generic logistics block (like Hamburg)
            return "Plan: 1. Reroute via Rotterdam. 2. Use air freight for urgent steel. 3. Notify clients of 2-day delay."
            
        elif self.name == "Critic":
            # Critic approves the plan for this mock demo
            return "APPROVED. The plan is feasible and cost-effective."
            
        elif self.name == "Implementer":
            # Simulates the execution step based on the plan
            return "SUCCESS: Executed Python script. Updated 'inventory.json' status for affected Items to 'IN TRANSIT - REROUTED'."

        return f"[Mock Output from {self.name}] Processed: {query}"

# --- TOOLS & MEMORY DEFINITIONS (Used for visual logging in UI) ---

def check_inventory_tool(location_keyword: str) -> str:
    """Simulates checking the internal inventory database."""
    print(f"    🏭 [Tool Call] Checking Inventory for: {location_keyword}...")
    # This mock function only exists to show the tool call in the console/logs, the Agent class handles the result.
    return "Inventory check simulated."

def check_severe_weather_tool(location: str) -> str:
    """Simulates checking for active severe weather alerts."""
    print(f"    🌩️ [Tool Call] Checking Severe Weather for: {location}...")
    return "Weather check simulated."

class MemoryBank:
    """Simulates the persistent memory for the Strategist."""
    def recall(self, query: str) -> str:
        print(f"    🧠 [Memory] Recalling past solutions for: {query}...")
        return "Memory recall simulated."

memory_bank = MemoryBank()

# --- AGENT DEFINITIONS (The Architecture) ---
# Instantiating the four agents using the mock class
watchtower_agent = Agent(
    name="Watchtower",
    instructions="Monitor news, use InventoryTool, and output RISK_ALERT or CLEAR."
)

strategist_agent = Agent(
    name="Strategist",
    instructions="Receive ALERTS, consult memory, and propose a mitigation plan."
)

critic_agent = Agent(
    name="Critic",
    instructions="Review the plan for feasibility, cost, and safety. Output APPROVED or REJECTED."
)

implementer_agent = Agent(
    name="Implementer",
    instructions="Execute the APPROVED plan by running database update code."
)

# --- GRADIO UI RUNNER (The Production Deployment) ---
def sentinel_ui_runner(news_input):
    """Orchestrates the four agents and provides real-time log output using Gradio's yield."""
    logs = []
    
    def log(message):
        timestamp = time.strftime("%H:%M:%S")
        logs.append(f"[{timestamp}] {message}")
        # Use yield to update the Gradio interface in real-time
        return "\n".join(logs)

    yield log(f"🔵 [System] Incoming News: \"{news_input}\"")
    time.sleep(0.5)
    
    # 1. Watchtower Agent Flow (Detection)
    yield log(f"📡 [Watchtower] Scanning news feed and consulting internal tools...")
    
    # Simulate Tool Calls visually based on common risk scenarios
    if "Hamburg" in news_input or "Strike" in news_input:
        yield log(f"   > 🛠️ Tool Call: check_inventory('Hamburg')")
    if "Florida" in news_input or "Hurricane" in news_input:
        yield log(f"   > 🛠️ Tool Call: check_inventory('Florida')")
        yield log(f"   > 🌩️ Tool Call: check_severe_weather('Florida')")
    if "Tokyo" in news_input:
        yield log(f"   > 🛠️ Tool Call: check_inventory('Tokyo')")
    
    time.sleep(1.5) # Simulate latency for tool execution and LLM reasoning
    
    impact = watchtower_agent.run(news_input)
    yield log(f"📝 [Watchtower Output]: {impact}")
    
    if "ALERT" not in impact:
        yield log("✅ System Status: GREEN (No Action Needed)")
        return

    # 2. Strategist Agent Flow (Planning)
    time.sleep(1.0)
    yield log(f"\n⚙️ [Strategist] Consulting Memory Bank...")
    
    # Simulate Memory Tool Call
    if "ALERT" in impact:
        memory_bank.recall("Risk Event") 
        yield log(f"   > 🧠 Memory Recall: Found successful mitigation strategy from past event.")
    
    time.sleep(1.5)
    plan = strategist_agent.run(impact)
    yield log(f"📋 [Strategist Draft]: {plan}")

    # 3. Critic Agent Flow (Self-Correction/Governance)
    time.sleep(1.0)
    yield log(f"\n⚖️ [Critic] Analyzing Plan Risk & Cost...")
    critique = critic_agent.run(plan) # Always APPROVED in this mock
    
    time.sleep(1.0)
    yield log(f"✅ [Critic Decision]: {critique}")

    # 4. Implementer Agent Flow (Level 5 Autonomy)
    time.sleep(1.0)
    if "APPROVED" in critique:
        yield log(f"\n🚀 [Implementer] Executing autonomous database updates...")
        execution_log = implementer_agent.run(plan)
        time.sleep(1.5)
        yield log(f"💾 [Execution Log]: {execution_log}")
    
    yield log(f"\n🎉 MISSION COMPLETE. Latency to Action: ~7.0s.")

# --- GRADIO INTERFACE SETUP ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🛡️ Supply Chain Sentinel: The War Room")
    gr.Markdown("Enter a breaking news headline to trigger the **Autonomous Multi-Agent System**.")
    
    with gr.Row():
        with gr.Column(scale=1):
            news_input = gr.Textbox(
                label="Incoming News Feed", 
                placeholder="e.g., 'Major strike declared at Hamburg Port.'",
                lines=2
            )
            run_btn = gr.Button("🚨 Analyze Threat", variant="primary")
            
            gr.Examples([
                "Local bake sale happening in Ohio.",
                "BREAKING: Major labor strike declared at Hamburg Port.",
                "URGENT: Hurricane Warning issued for Florida Coast.",
                "BREAKING: 7.0 Magnitude Earthquake strikes Tokyo."
            ], inputs=news_input)
            
        with gr.Column(scale=2):
            log_output = gr.Code(label="Agent Orchestration Logs (A2A Trace)", language="shell", interactive=False)

    run_btn.click(fn=sentinel_ui_runner, inputs=news_input, outputs=log_output)

# Launch logic
if __name__ == "__main__":
    print("🚀 Launching War Room UI. Open the provided link in your browser.")
    # To run this, you need to install Gradio: pip install gradio
    demo.queue().launch(share=True)
