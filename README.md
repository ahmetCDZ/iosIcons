iOS Uygulama İkon Oluşturma

Bu Python betiği, bir iOS uygulaması için çeşitli ikon boyutlarını oluşturmak için bir görüntünün boyutunu otomatik olarak değiştirme işlemini otomatikleştirir.

Önkoşullar

Sisteminizde Python kurulu olmalıdır.
PIL (Python Imaging Library) kurulu olmalıdır. Pip aracılığıyla kurabilirsiniz:
Kodu kopyala
pip install Pillow

Kullanım
Bu depoyu yerel makinenize klonlayın veya indirin.
Betiği (icon_resizer.py) bir metin düzenleyicide açın.
sourcePath değişkenini kaynak görüntünün yoluna değiştirin.
resultPath değişkenini yeniden boyutlandırılan ikonların kaydedileceği dizine değiştirin.
Betiği çalıştırın.

İkon Boyutları
Betiğin oluşturduğu ikonlar şu boyutlarda olur:

iPhoneApp_20x20@1x
iPhoneApp_20x20@2x
iPhoneApp_20x20@3x
iPhoneApp_29x29@1x
iPhoneApp_29x29@2x
iPhoneApp_29x29@3x
iPhoneApp_40x40@1x
iPhoneApp_40x40@2x
iPhoneApp_40x40@3x
iPhoneApp_60x60@2x
iPhoneApp_60x60@3x
iPhoneApp_76x76@1x
iPhoneApp_76x76@2x
iPhoneApp_83.5x83.5@2x
iPhoneApp_1024x1024@1x

Örnek
Varsayalım ki kaynak görüntünüz masaüstünde resim.jpeg adında ve iOS uygulamanız için ikonlar oluşturmak istiyorsunuz. Betiği çalıştırdıktan sonra, yeniden boyutlandırılmış ikonlar belirttiğiniz resultPath dizininde masaüstünüzde kaydedilecektir.

Teşekkürler

Bu betik, görüntüleri yeniden boyutlandırmak için Python Imaging Library (PIL) kullanır.

Bu README'yi projenize özgü herhangi bir ek bilgi veya talimatı içerecek şekilde daha fazla özelleştirebilirsiniz. Başka bir yardıma ihtiyacınız olursa bana bildirin!
