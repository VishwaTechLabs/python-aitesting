def exact_match(expected, actual):
    return expected.strip().lower() == actual.strip().lower()

score = exact_match("PASS", "pass")
print("score:", score)
assert score is True
