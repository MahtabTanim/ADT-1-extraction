import cohere

co = cohere.Client("JILxToixtFPm6yk1DOtzCaV74TUB5S0MQe6uEgDb")


def extract_brief_from_attachment(text):
    lines = text.splitlines()
    summary = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if any(
            keyword in line.lower()
            for keyword in ["appointed", "subject", "meeting", "date", "auditor"]
        ):
            summary.append(line)
        if len(summary) >= 5:
            break

    return " ".join(summary).strip()[:400]


def get_summary(data, attachment_texts=None):

    prompt = (
        "Summarize the following statutory auditor appointment filing in 5-10 simple, human-readable lines, "
        "using appropriate line breaks:\n\n"
        f"Company: {data['company_name']}\n"
        f"Auditor: {data['auditor_name']}\n"
        f"Appointment Type: {data['appointment_type']}\n"
        f"Appointment Date: {data['appointment_date']}\n"
        f"Approved in AGM: {data['auditor_appointed_in_agm']}\n"
        f"AGM Date: {data['agm_date']}\n"
        f"Accounting Period: {data['accounting_period_from']} to {data['accounting_period_to']}\n"
        f"Duration: {data['number_of_years_appointed']} years\n"
        f"Joint Auditors: {data['joint_auditors']}\n"
    )
    if attachment_texts and len(attachment_texts) > 0:
        prompt += "\nRelevant points from attachments:\n"
        for i, text in enumerate(attachment_texts, start=1):
            brief = extract_brief_from_attachment(text)
            prompt += f"Attachment {i}: {brief}\n"
    prompt += "\nSummary:\n"

    response = co.generate(
        model="command",
        prompt=prompt.strip(),
        max_tokens=100,
        temperature=0.5,
        stop_sequences=["\n\n", "\nSummary:"],
    )

    summary = response.generations[0].text.strip()
    return summary
