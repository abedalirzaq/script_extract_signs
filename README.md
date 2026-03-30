# Traffic Signs HTML Extractor

**الهدف:**
لدينا محتوى تعليمي للشواخص في ملفات HTML 
هذا السكريبت مصمم لسحب البيانات من ملف الhtml ووضعها بطريقة منطمة في ملف json
## طريقة التشغيل
1. إذا لم تكن البيئة الافتراضية مفعلة بعد، أنشئها:

```bash
python3 -m venv env

فعّل البيئة الافتراضية:

source env/bin/activate

ثبّت المكتبة المطلوبة:

pip install beautifulsoup4

شغّل السكريبت:

python3 extract_signs.py

بعد التشغيل، سيتم إنشاء ملف output.json يحتوي على الشواخص مع روابط الصور.