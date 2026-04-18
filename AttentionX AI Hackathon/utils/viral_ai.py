def compute_viral_score(segment):
    text = segment["text"].lower()

    score = 0

    keywords = [
        "mistake", "secret", "never", "always",
        "truth", "important", "life",
        "success", "failure", "learn"
    ]

    for w in keywords:
        if w in text:
            score += 2

    score += min(len(text.split()) / 20, 3)

    return score