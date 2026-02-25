def test_token_format():
    fake_token = "MON_TOKEN_FAKEFAKEFAKE"  # Faux positif intentionnel
    assert fake_token.startswith("MON_TOKEN_")
    print("Format OK")
