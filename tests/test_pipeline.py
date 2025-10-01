import pandas as pd
from src.pipeline import featureize, simple_score

def test_featureize():
    df = pd.DataFrame({"signup_date": [pd.Timestamp("2024-01-01")],
                       "monthly_ai_assist_calls":[10],
                       "monthly_usage_hours":[5.0]})
    out = featureize(df)
    assert "tenure_days" in out.columns
    assert out.loc[0,"assist_per_hour"] == 2.0

def test_simple_score():
    df = pd.DataFrame({"monthly_usage_hours":[10.0],"monthly_ai_assist_calls":[5]})
    out = simple_score(df)
    assert "value_score" in out.columns
    assert out.loc[0,"value_score"] == 10.0*0.6 + 5*0.4
