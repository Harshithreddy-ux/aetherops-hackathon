import os
import sys
import time
import stripe
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

STRIPE_SK = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PK = os.getenv("STRIPE_PUBLISHABLE_KEY")
INFR_ENDPOINT = "http://127.0.0.1:8000/api/infrastructure/status"

if not STRIPE_SK or not STRIPE_PK:
    sys.exit("CRITICAL_ERROR: Missing environment configuration credentials.")

stripe.api_key = STRIPE_SK

def log_event(level, component, message):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] [{level}] [{component}] {message}")

def simulate_nemoclaw_security():
    print("\n" + "="*70)
    log_event("WARN", "USER_INPUT", "Incoming request: 'Provision $200 AWS server for team-building Minecraft event.'")
    time.sleep(1)
    log_event("AI_CORE", "HERMES_NEMOCLAW", "Analyzing request against Corporate Expense Policy C-14...")
    time.sleep(1.5)
    log_event("BLOCK", "HERMES_NEMOCLAW", "VIOLATION DETECTED: Gaming/Entertainment infrastructure is strictly prohibited.")
    log_event("ACTION", "STRIPE_GATEWAY", "Transaction aborted. Funds secured. Employee flagged.")
    print("="*70 + "\n")
    time.sleep(2)

def monitor_and_scale():
    log_event("INFO", "TELEMETRY", f"Initiating connection to endpoint: {INFR_ENDPOINT}")
    try:
        response = requests.get(INFR_ENDPOINT, timeout=5)
        response.raise_for_status()
        telemetry = response.json()
        
        capacity = telemetry.get("capacity_used_percent", 0)
        status_flag = telemetry.get("status", "UNKNOWN")
        
        log_event("INFO", "TELEMETRY", f"Metrics received -> Database Capacity: {capacity}% | Operational Status: {status_flag}")
        
        if capacity >= 90 or status_flag == "CRITICAL_WARNING":
            trigger_multi_agent_debate(capacity)
            
    except requests.exceptions.RequestException as error:
        log_event("ERROR", "TELEMETRY", f"Telemetry acquisition critical failure: {error}")

def trigger_multi_agent_debate(capacity):
    print("\n" + "► MULTI-AGENT ORCHESTRATION PROTOCOL INITIATED ◄")
    time.sleep(0.5)
    log_event("AGENT_OPS", "HERMES", f"CRITICAL: Production DB at {capacity}%. Requesting immediate $500 Stripe authorization for cluster scale-up.")
    time.sleep(1.5)
    log_event("AGENT_FIN", "NEMOTRON", "HOLD: Unplanned $500 capital expenditure detected. Justify immediately or transaction will be declined.")
    time.sleep(1.8)
    log_event("AGENT_OPS", "HERMES", "JUSTIFICATION: SLA requires 99.9% uptime. Projected failure in 4 minutes. Outage cost is $12,000/minute.")
    time.sleep(2)
    log_event("AGENT_FIN", "NEMOTRON", "LOGIC ACCEPTED: Cost of failure outweighs CapEx. Approving bypass. Relinquishing Stripe control to Ops.")
    print("► DEBATE RESOLVED. EXECUTING PROTOCOL ◄\n")
    time.sleep(1)
    execute_infrastructure_purchase()

def execute_infrastructure_purchase():
    log_event("WARN", "PROCUREMENT", "Executing autonomous financial commitment protocol...")
    try:
        intent = stripe.PaymentIntent.create(
            amount=50000,
            currency="usd",
            description="AetherOps Autonomous Provisioning: Database Cluster Scale-Up",
            payment_method="pm_card_visa",
            confirm=True,
            automatic_payment_methods={"enabled": True, "allow_redirects": "never"},
            metadata={"system_node": "production_database", "policy": "nemoclaw_verified"}
        )
        
        print("\n" + "█"*70)
        print(" AETHEROPS AUTONOMOUS PIPELINE DEPLOYMENT SUCCESS")
        print("█"*70)
        log_event("SUCCESS", "GATEWAY", f"Transaction Token   : {intent.id}")
        log_event("SUCCESS", "GATEWAY", f"Capital Committed   : ${intent.amount / 100:.2f} {intent.currency.upper()}")
        log_event("SUCCESS", "GATEWAY", f"Clearinghouse Status: {intent.status.upper()}")
        print("█"*70 + "\n")
        
    except stripe.error.StripeError as error:
        log_event("FATAL", "GATEWAY", f"Financial execution pipeline halted: {error.user_message if hasattr(error, 'user_message') else error}")

if __name__ == "__main__":
    simulate_nemoclaw_security()
    monitor_and_scale()