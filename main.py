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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] [{level}] [{component}] {message}")

def monitor_and_scale():
    log_event("INFO", "TELEMETRY", f"Initiating connection to endpoint: {INFR_ENDPOINT}")
    try:
        response = requests.get(INFR_ENDPOINT, timeout=5)
        response.raise_for_status()
        telemetry = response.json()
        
        capacity = telemetry.get("capacity_used_percent", 0)
        status_flag = telemetry.get("status", "UNKNOWN")
        
        log_event("INFO", "TELEMETRY", f"Metrics received -> Database Capacity: {capacity}% | Operational Status: {status_flag}")
        
        # Simulate Hermes Autonomous Reasoning Engine Evaluation
        print("\n" + "="*60)
        log_event("AI_CORE", "HERMES_THOUGHT", "Analyzing systemic telemetry data...")
        time.sleep(0.8)
        log_event("AI_CORE", "HERMES_THOUGHT", f"Observation: Production database cluster is operating at {capacity}% volume.")
        time.sleep(0.6)
        log_event("AI_CORE", "HERMES_THOUGHT", f"Risk Assessment: Exceeds critical SLA safety margin (90%). Hazard level: HIGH.")
        time.sleep(0.6)
        log_event("AI_CORE", "HERMES_THOUGHT", "Policy Evaluation: NemoClaw rule compliance active. Automated resolution authorized.")
        time.sleep(0.6)
        log_event("AI_CORE", "HERMES_THOUGHT", "Action Selected: Call Tool [stripe.PaymentIntent.create] to provision additional cluster resources.")
        print("="*60 + "\n")
        
        if capacity >= 90 or status_flag == "CRITICAL_WARNING":
            execute_infrastructure_purchase()
            
    except requests.exceptions.RequestException as error:
        log_event("ERROR", "TELEMETRY", f"Telemetry acquisition critical failure: {error}")

def execute_infrastructure_purchase():
    log_event("WARN", "PROCUREMENT", "Executing autonomous financial commitment protocol...")
    try:
        intent = stripe.PaymentIntent.create(
            amount=50000,
            currency="usd",
            description="AetherOps Autonomous Provisioning: Database Cluster Scale-Up",
            payment_method="pm_card_visa",
            confirm=True,
            automatic_payment_methods={
                "enabled": True,
                "allow_redirects": "never"
            },
            metadata={
                "system_node": "production_database",
                "policy_compliance": "nemoclaw_verified",
                "orchestrator": "hermes_core"
            }
        )
        
        print("\n" + "█"*60)
        print(" AETHEROPS AUTONOMOUS PIPELINE PIPELINE DEPLOYMENT SUCCESS")
        print("█"*60)
        log_event("SUCCESS", "GATEWAY", f"Transaction Remote Reference: {intent.id}")
        log_event("SUCCESS", "GATEWAY", f"Capital Committed            : ${intent.amount / 100:.2f} {intent.currency.upper()}")
        log_event("SUCCESS", "GATEWAY", f"Clearinghouse Status         : {intent.status.upper()}")
        print("█"*60 + "\n")
        
    except stripe.error.StripeError as error:
        log_event("FATAL", "GATEWAY", f"Financial execution pipeline halted: {error.user_message if hasattr(error, 'user_message') else error}")

if __name__ == "__main__":
    monitor_and_scale()