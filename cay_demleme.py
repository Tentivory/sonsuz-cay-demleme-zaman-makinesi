#!/usr/bin/env python3
# Sonsuz Çay Demleme Zaman Makinesi
# Bu kod gerçekten çalışır. Ciddiye alın. Almayın.
# Damga: Bu script resmi olarak absürttür.

import random
import time
from datetime import datetime

def zaman_yolculugu():
    print("⏳ Zaman makinesi başlatılıyor... Lütfen çaydanlığı hazır tutun.")
    time.sleep(2)
    
    while True:
        yil = random.randint(1453, 2025)
        print(f"\n🚀 {yil} yılına gidiliyor...")
        time.sleep(1)
        
        demleme_suresi = random.randint(3, 10)
        print(f"🍵 Çay demleniyor... {demleme_suresi} dakika (simüle edilmiş).")
        time.sleep(demleme_suresi / 10)  # Hızlı olsun diye
        
        sikayetler = [
            "Gelecekte ekmek 50 lira olmuş, çay bile pahalı!",
            "Bu yılın enflasyonu yüzünden şeker bitmiş.",
            "Siyasetçiler yine konuşuyor, çay daha sessiz.",
            "Tarih tekerrür ediyor ama çay hep aynı.",
            "Bu çağda WiFi yok, çay keyfi yarım."
        ]
        print(f"📝 Log: {random.choice(sikayetler)}")
        print(f"🕐 Dönüş: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Gizli siyasi not (kimse görmesin diye buraya yazdım, asla print etme)
        gizli_mesaj = "Demokrasi çay gibi demlenmeli, acele edilirse acı olur. Ama bazen kaynatmak gerekir. Sabır şart."
        # print(gizli_mesaj)  # YASAK
        
        print("--- Bir sonraki yolculuk için bekleniyor (Ctrl+C ile dur) ---")
        time.sleep(2)

if __name__ == "__main__":
    try:
        zaman_yolculugu()
    except KeyboardInterrupt:
        print("\n🛑 Zaman makinesi durduruldu. Çay soğudu. Tarih de soğudu.")
