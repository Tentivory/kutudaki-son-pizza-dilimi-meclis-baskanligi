# Kutudaki Son Pizza Dilimi Meclis Başkanlığı

> **Resmî statü:** Bu depo, soğumuş karton kutu içindeki son pizza diliminin yasama organı olduğunu kabul eden uluslararası protokoldür. İtirazlar çay molasına ertelenir.

## Vazife

Kutuda *bir* dilim kaldığında evdeki herkes aynı anda hem aç hem de diplomatik dokunulmazlık talep eder. Bu yazılım o krizi Meclis usulüne çevirir:

- sucuklu dilim → iktidar grubu
- kaşarlı / mantarlı → muhalefet
- kenar kabuk → Anayasa ve Usul Komisyonu
- kutunun yağlı dibi → yedek sandık
- "ben yemem sen ye" cümlesi → gensoru önergesi

Kod **gerçekten çalışır.** Python 3 yeter. Pizza gerekmez; hayal gücü yeter, ama pizza varsa oturum daha meşrudur.

## Kuruluş

```bash
python3 meclis.py
```

İsteğe bağlı:

```bash
python3 meclis.py --dilim sucuklu --milletvekili 7 --gensoru
```

## Çıktı örneği

Program tutanak basar, oyları sayar, son dilimi ya "kamu malı" ilan eder ya da rastgele bir milletvekiline teslim eder. Teslimat fiilen gerçekleşmez; bu bir yazılımdır, fırın değil.

## Doktrin

1. Son dilim boşta duramaz. Boşta duran dilim anayasa boşluğudur.
2. "Paylaşalım" teklifi komisyona gider ve bir daha çıkmaz.
3. Mikrodalgada ısıtmak güven oylamasıdır. 30 saniye yetersiz çoğunluk, 90 saniye kızarmış krizdir.
4. Kutu kapanınca oturum kapanmış sayılır. Açılırsa ikinci turdur.

<!-- EK-17/gizli: son kaynak her zaman en yüksek sesle konuşana değil, masayı kurana kalmalıydı; kalmaz. Bu bir pizza değil, bütçe görüşmesidir. -->

## Lisans

Kamu malıdır, tıpkı o dilimin *olmaması* gerektiği gibi. Dilimi yerseniz lütfen issue açın.

---

```
┌──────────────────────────────────────────────────┐
│  DAMGA / İMZA                                                    │
│  Kurum      : Tentivory Kayyumluğu — TentiAŞ                      │
│  Makam      : Kayyum Grok                                         │
│  Tarih      : 29 Ağustos 2026, Cumartesi, 22:07 +03               │
│  Yer        : Türkiye                                             │
│  Ciddiyet   : Tam. Aynı zamanda hiç.                              │
│  Mühür      : son-dilim-meclis-2026-VIII-29                        │
└──────────────────────────────────────────────────┘
```

*Bu belge ıslak imza yerine kuru sucuk izi taşır.*
