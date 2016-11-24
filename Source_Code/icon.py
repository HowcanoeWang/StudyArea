img = b'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'