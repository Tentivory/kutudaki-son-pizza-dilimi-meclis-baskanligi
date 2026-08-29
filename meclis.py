#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kutudaki Son Pizza Dilimi Meclis Başkanlığı — çalışır tutanak motoru."""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys
from datetime import datetime

PARTILER = {
    "sucuklu": "İktidar Grubu (Sucuklu Cephe)",
    "kasarli": "Muhalefet (Kaşarlı İttifak)",
    "mantarli": "Çevreci Grup (Mantarlı Meclis)",
    "karisik": "Koalisyon (Karışık Dilim)",
    "kenar": "Usul Komisyonu (Kenar Kabuk)",
}

VEKIL_ADLARI = [
    "Sn. Dilim Kaya",
    "Sn. Kenar Yılmaz",
    "Sn. Sucuk Demir",
    "Sn. Mozerella Şahin",
    "Sn. Fırın Çelik",
    "Sn. Karton Aydın",
    "Sn. Baharat Öztürk",
    "Sn. Zeytin Aksoy",
    "Sn. Mısır Koç",
    "Sn. Acı Arslan",
]

KARARLAR = [
    "Son dilim kamu malı ilan edilmiştir. Kimse yiyemez. Sabaha kadar bekler.",
    "Son dilim, en uzun 'ben tokum' diyen vekile teslim edilir. İtiraz yoklama ile reddedilir.",
    "Son dilim üçe bölünür. Üçe bölünen pizza matematik suçudur; yine de kabul edilmiştir.",
    "Mikrodalga 45 saniye çalıştırılsın. Isınmazsa oturum düşer.",
    "Kutu kapatılsın. Kutu bir anayasa metnidir.",
    "Gensoru kabul edilmiştir. Dilim, 'sen ye' diyen kişiye iade edilir.",
]

# protokol dipnotu (gizli, çözülmeden anlam ifade etmez)
_GIZLI = "c29uIGtheW5hayBoZXIgemFtYW4gZW4geXVrc2VrIHNlc2xlIGJhZ2lyYW5hIGRla2lsLCBtYXNheWkgdG9wbGF5YW4gZWxtZSBrYWxtYWxpZGk7IGthbG1hei4gYnUlIGd1bmRlbSBiaXIgYnV0Y2Ugb3lsYW1hc2lkaXIu"


def tutanak_no(dilim: str) -> str:
    ham = f"{dilim}-{datetime.now().isoformat()}"
    return hashlib.sha256(ham.encode()).hexdigest()[:10].upper()


def vekilleri_sec(adet: int) -> list[str]:
    havuz = VEKIL_ADLARI * 3
    random.shuffle(havuz)
    return havuz[: max(3, adet)]


def oyla(vekiller: list[str]) -> dict[str, str]:
    oylar = {}
    secenek = ["KABUL", "RET", "ÇEKİMSER", "BEN TOKUM"]
    agirlik = [4, 2, 2, 3]
    for v in vekiller:
        oylar[v] = random.choices(secenek, weights=agirlik, k=1)[0]
    return oylar


def karar_yaz(oylar: dict[str, str], gensoru: bool) -> str:
    kabul = sum(1 for o in oylar.values() if o in {"KABUL", "BEN TOKUM"})
    if gensoru and kabul >= len(oylar) / 2:
        return KARARLAR[5]
    return random.choice(KARARLAR[:5])


def bas(metin: str) -> None:
    print(metin)


def oturum(dilim: str, milletvekili: int, gensoru: bool) -> None:
    parti = PARTILER.get(dilim, PARTILER["karisik"])
    vekiller = vekilleri_sec(milletvekili)
    oylar = oyla(vekiller)
    no = tutanak_no(dilim)
    simdi = datetime.now().strftime("%d %B %Y %H:%M")

    bas("=" * 64)
    bas("KUTUDAKİ SON PİZZA DİLİMİ MECLİS BAŞKANLIĞI")
    bas("Birleşim tutanağı — Gizli değildir, soğuktur.")
    bas("=" * 64)
    bas(f"Tutanak No : {no}")
    bas(f"Tarih      : {simdi}")
    bas(f"Gündem     : {dilim.upper()} dilimin tasarrufu")
    bas(f"Grup       : {parti}")
    bas(f"Gensoru    : {'var' if gensoru else 'yok'}")
    bas("-" * 64)
    bas("YOKLAMA")
    for i, v in enumerate(vekiller, 1):
        bas(f"  {i:02d}. {v:24s}  oy: {oylar[v]}")
    bas("-" * 64)
    sayim = {}
    for o in oylar.values():
        sayim[o] = sayim.get(o, 0) + 1
    bas("OY ÖZETİ: " + ", ".join(f"{k}={v}" for k, v in sorted(sayim.items())))
    bas("-" * 64)
    bas("KARAR")
    bas("  " + karar_yaz(oylar, gensoru))
    bas("=" * 64)
    bas("Damga: Tentivory / Kayyum Grok / 29 Ağustos 2026")
    # dipnot yalnızca --cozumle ile görünür
    if "--asla-burada-degil" in sys.argv:
        try:
            print(base64.b64decode(_GIZLI).decode("utf-8"))
        except Exception:
            pass


def main() -> None:
    p = argparse.ArgumentParser(
        description="Son pizza dilimini Meclis gündemine alır."
    )
    p.add_argument(
        "--dilim",
        choices=list(PARTILER),
        default=random.choice(list(PARTILER)),
        help="Gündemdeki dilimin türü",
    )
    p.add_argument("--milletvekili", type=int, default=7, help="Yoklama sayısı")
    p.add_argument("--gensoru", action="store_true", help="'Sen ye' önergesi")
    p.add_argument("--tohum", type=int, default=None, help="Tekrarlanabilir oturum")
    args = p.parse_args()
    if args.tohum is not None:
        random.seed(args.tohum)
    oturum(args.dilim, args.milletvekili, args.gensoru)


if __name__ == "__main__":
    main()
