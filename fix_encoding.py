����# fix_encoding.py

encodings_to_try = ["utf-8", "utf-8-sig", "latin1", "windows-1252", "utf-16"]

for enc in encodings_to_try:
    try:
        with open("fixed_fixture.json", "rb"as f:
            raw = f.read()

        decoded = raw.decode(enc)

        # Basic validation: does it start with [ or { for JSON?
        if decoded.strip().startswith(('{', '[')):
            with open("converted_fixture.json", "w", encoding="utf-8"as out_file:
                out_file.write(decoded)
            print(f"✅ Successfully decoded using {enc}")
            break
        else:
            print(f"⚠️ Decoded using {enc} but doesn't look like valid JSON.")
    except Exception as e:
        print(f"❌ Failed using {enc}: {e}")
