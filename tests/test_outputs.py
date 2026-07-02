from pathlib import Path
import json

def test_report_exists_and_valid():
    """
    Verifies the success criterion from instruction.md:
    "The agent must generate a valid JSON report file at /app/report.json."
    """
    path = Path("/app/report.json")
    assert path.exists(), "no report.json found"
    
    try:
        with open(path) as f:
            data = json.load(f)
    except Exception as e:
        assert False, f"Failed to parse JSON: {e}"


def test_report_contents():
    """
    Verifies the success criterion from instruction.md:
    "The report must contain correct values for total_requests, unique_ips, and top_path."
    """
    path = Path("/app/report.json")
    with open(path) as f:
        data = json.load(f)
        
    assert data.get("total_requests") == 6, f"Expected 6 requests, got {data.get('total_requests')}"
    assert data.get("unique_ips") == 3, f"Expected 3 unique IPs, got {data.get('unique_ips')}"
    assert data.get("top_path") == "/index.html", f"Expected top path '/index.html', got {data.get('top_path')}"
