# Tutorial: Chay mo hinh phat hien JavaScript Obfuscated lan dau

Tai lieu nay giup nguoi moi chay duoc mo hinh tu dau den cuoi va doc duoc ket qua danh gia.

## Muc tieu hoc
Sau khi hoan thanh, ban se:
- Chay duoc pipeline huan luyen + kiem thu.
- Hieu cac chi so chinh (Accuracy, Precision, Recall, F1).
- Xac nhan mo hinh hoat dong dung trong moi truong cuc bo.

## Truoc khi bat dau
- Da cai Python 3.
- Co thu vien `scikit-learn`.
- Trong project co cac thu muc:
  - `JavascriptSamples/` (mau JavaScript thuong)
  - `JavascriptSamplesObfuscated/` (mau JavaScript obfuscated)
- Co file `run_detection.py`.

## Buoc 1: Mo terminal tai thu muc project
Vi du:
```bash
cd /home/ubuntu/ATTTML
```

## Buoc 2: Cai phu thuoc (neu chua co)
```bash
pip install scikit-learn
```

## Buoc 3: Chay script huan luyen va kiem thu
```bash
python3 run_detection.py
```

## Buoc 4: Doc ket qua
Script se in:
- Accuracy
- Confusion Matrix
- Precision
- Recall (Sensitivity)
- Specificity
- F1-Score
- Classification Report

Vi du cach hieu nhanh:
- Accuracy cao: tong the du doan dung nhieu.
- Precision cao: khi du doan "obfuscated", ty le dung cao.
- Recall cao: phat hien duoc nhieu ma obfuscated that.
- F1 cao: Precision va Recall can bang.

## Buoc 5: Kiem tra nhanh chat luong mo hinh
Neu Accuracy/Precision/Recall deu quanh hoac tren 0.90, mo hinh dang hoat dong tot o muc co ban.
Neu Recall thap, can chu y vi mo hinh bo sot ma obfuscated.

## Ban da hoan thanh
Ban da chay duoc toan bo pipeline va hieu cach doc ket qua danh gia chinh.
