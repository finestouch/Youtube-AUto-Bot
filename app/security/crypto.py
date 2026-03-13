from __future__ import annotations

import base64
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class Aes256Cipher:
    """AES-256-GCM helper for API key encryption at rest."""

    def __init__(self, key: bytes | None = None) -> None:
        self._key = key or AESGCM.generate_key(bit_length=256)
        self._cipher = AESGCM(self._key)

    @property
    def key_b64(self) -> str:
        return base64.b64encode(self._key).decode("utf-8")

    def encrypt(self, plaintext: str) -> str:
        nonce = os.urandom(12)
        ciphertext = self._cipher.encrypt(nonce, plaintext.encode("utf-8"), None)
        return base64.b64encode(nonce + ciphertext).decode("utf-8")

    def decrypt(self, encoded: str) -> str:
        blob = base64.b64decode(encoded)
        nonce, ciphertext = blob[:12], blob[12:]
        return self._cipher.decrypt(nonce, ciphertext, None).decode("utf-8")
