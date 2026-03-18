# How-to: Danh gia du lieu training/test cho mo hinh hien tai

Tai lieu nay huong dan cach danh gia nhanh chat luong du lieu train/test va rui ro thuong gap.

## Khi nao dung tai lieu nay
Dung khi ban muon tra loi:
- Du lieu co can bang giua 2 lop khong?
- Chia train/test co hop ly khong?
- Ket qua hien tai co dang tin de dung thu chua?

## Buoc 1: Kiem tra so luong mau theo lop
Dem so file trong:
- `JavascriptSamples/` (Normal JS)
- `JavascriptSamplesObfuscated/` (Obfuscated JS)

Muc tieu:
- Khong lech qua manh giua 2 lop.
- Neu lech, nen giu `class_weight="balanced"` nhu hien tai.

## Buoc 2: Xac nhan cach chia du lieu
Trong `run_detection.py`, du lieu dang chia bang:
- `test_size=0.33`
- `random_state=42`

Danh gia:
- 67% train / 33% test la chap nhan duoc cho baseline.
- `random_state` giup ket qua tai lap.

## Buoc 3: Chay danh gia mo hinh
```bash
python3 run_detection.py
```

## Buoc 4: Doc confusion matrix truoc tien
Quy uoc:
- TP: Obfuscated du doan dung
- TN: Normal du doan dung
- FP: Normal bi nham thanh Obfuscated
- FN: Obfuscated bi bo sot

Uu tien:
- Giam FN neu muc tieu thien ve bao mat (tranh bo sot ma doc/an).

## Buoc 5: Danh gia theo nguong thuc dung
Goi y nhanh:
- Accuracy >= 0.90: tot cho baseline.
- Recall lop Obfuscated >= 0.90: phu hop bai toan phat hien.
- Precision lop Obfuscated >= 0.90: giam canh bao gia.
- F1 lop Obfuscated >= 0.90: can bang tong the.

## Buoc 6: Ket luan va hanh dong
Neu metric on:
- Ghi nhan ket qua baseline.
- Luu cau hinh hien tai lam moc so sanh.

Neu metric chua on:
- Tang du lieu lop yeu.
- Dung cross-validation.
- Tuning tham so RandomForest.
- Phan tich cac mau bi sai (FP/FN).

## Ket qua mong doi
Ban co the ket luan ro:
- Chat luong du lieu train/test hien tai.
- Muc tin cay cua mo hinh baseline.
- Huong cai thien uu tien tiep theo.
