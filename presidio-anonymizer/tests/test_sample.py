from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Text check
    assert res.text == "My name is BIP."

    # Items list checks
    assert isinstance(res.items, list)
    assert len(res.items) == 1

    it = res.items[0]
    assert it.start == 11
    assert it.end == 14          # "BIP" length = 3 → end becomes 14
    assert it.entity_type == "PERSON"
    assert it.text == "BIP"
    assert it.operator == "replace"
