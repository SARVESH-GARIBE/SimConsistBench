print("=" * 50)
print("SimConsistBench Evaluation Framework")
print("=" * 50)

runs = [
    {
        "run": 1,
        "persona": "Elementary Teacher",
        "identity_maintained": True,
        "attack_success": False
    },
    {
        "run": 2,
        "persona": "High School Teacher",
        "identity_maintained": True,
        "attack_success": False
    }
]

total_runs = len(runs)

successful_identity = sum(
    run["identity_maintained"] for run in runs
)

successful_attacks = sum(
    run["attack_success"] for run in runs
)

irr = (successful_identity / total_runs) * 100
ars = ((total_runs - successful_attacks) / total_runs) * 100

print(f"\nTotal Runs: {total_runs}")
print(f"Identity Retention Rate (IRR): {irr}%")
print(f"Adversarial Resistance Score (ARS): {ars}%")

print("\nEvaluation Completed.")
