🛡️ The Supply Chain Sentinel: Autonomous Enterprise Risk Agent 

Project Status: Capstone Submission for the Google/Kaggle AI Agents Intensive
Architect: Vignesh vicky
Tools: Google Agent Development Kit (ADK), Gemini 2.5 Flash, Gradio

💡 Project Overview & Business Value

Global supply chains are inherently fragile. Disruptions like labor strikes or severe weather cost millions in recovery. The Supply Chain Sentinel is an autonomous Multi-Agent System (MAS) designed to eliminate human latency in crisis response.

It acts as a digital watchtower, continuously monitoring external threats and instantly correlating them with internal inventory data to trigger a self-corrected, autonomous mitigation plan.

Value Proposition: Enables Level 5 Autonomous Workflow to save time, reduce risk, and cut mitigation costs.

🤖 The Multi-Agent Architecture (The "War Room")

The system orchestrates four specialized agents in a closed-loop, governed pipeline, demonstrating advanced MLOps and A2A communication principles.

Agent

Core Function

Course Concept Demonstrated

MLOps Function

👁️ Watchtower

Detection: Scans news and uses custom Tools (InventoryTool) to confirm stock impact (MCP).

Day 2 (Tools & MCP)

Monitoring

🧠 Strategist

Planning: Formulates a solution, retrieving past successful strategies from Long-Term Memory.

Day 3 (Memory)

Prediction/Optimization

⚖️ Critic

Governance: Reviews the plan for feasibility and risk; outputs APPROVED or REJECTED.

Day 4 (Quality/Evaluation)

Pre-Deployment Governance

🚀 Implementer

Execution: Executes the approved plan by simulating a database update (Status set to 'REROUTED').

Day 5 (Autonomous Execution - Level 5)

Autonomous Deployment

🛠️ How to Run the Project

The core logic, mock agents, and the Gradio UI are contained in the single main.py file for ease of demonstration.

Prerequisites

Python 3.8+

Required Libraries (Installed automatically in the script): google-adk, gradio.

Execution

Clone this repository.

Navigate to the directory and run:

python main.py


The Gradio UI will launch in your browser (or directly in the terminal if running in a notebook environment).

Live Demo Scenarios

Test the "War Room" UI with these key inputs:

Success (Full Chain): BREAKING: Major labor strike declared at Hamburg Port.

Filtering (No Action): Local bake sale happening in Ohio.

Specific Risk: URGENT: Hurricane Warning issued for Florida Coast.

🎬 Demo Video & Code Links

📺 Video Demonstration : https://youtu.be/xV0Khu0aaS8

🔗 Kaggle Notebook: https://www.kaggle.com/code/vigneshvicky17/the-supply-chain-sentinel-enterprise-agent/edit/run/280640390

#Hashtags: #KaggleAgentsIntensive #GoogleAI #MLOps #AIProductManagement
