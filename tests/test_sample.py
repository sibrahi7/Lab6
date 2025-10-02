from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer_bond_example():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Required asserts
    assert res.text == "My name is BIP."
    assert len(res.items) == 1
    assert res.items[0].start == 11
    assert res.items[0].end == 14
