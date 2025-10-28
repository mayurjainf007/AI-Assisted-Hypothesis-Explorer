import os
import pandas as pd

def summarize_dataframe(df: pd.DataFrame, question: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            from langchain_openai import ChatOpenAI
            from langchain.prompts import ChatPromptTemplate
            llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL","gpt-4o-mini"), temperature=0.2)
            cols = ", ".join(df.columns.astype(str))
            sample = df.head(10).to_dict(orient="records")
            prompt = ChatPromptTemplate.from_template(
                "You are a bioinformatics research assistant. The user asks: '{q}'. "
                "Dataframe columns: {cols}. First 10 rows: {rows}. "
                "Write a concise, bullet-point summary of key findings with simple stats and a short hypothesis."
            )
            return llm.invoke(prompt.format_messages(q=question, cols=cols, rows=sample)).content
        except Exception:
            pass
    desc = df.describe(include="all", datetime_is_numeric=True).to_string()
    hyp = "- Hypothesis: Variables with highest variance may drive response; stratify by 'diagnosis' or 'treatment' if present."
    return f"""Heuristic Summary (no LLM used):\n\nBasic stats:\n{desc}\n\n{hyp}\n"""
