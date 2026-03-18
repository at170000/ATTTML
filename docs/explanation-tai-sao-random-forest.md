# Explanation: Vi sao pipeline `HashingVectorizer + TF-IDF + RandomForest` phu hop bai toan nay

## Boi canh
Bai toan la phat hien ma JavaScript da obfuscate. Du lieu la van ban ma nguon, khong phai anh hay so lieu cau truc san.

## Vi sao dung dac trung ky tu n-gram
Obfuscated code thuong co cac pattern ky tu dac trung:
- Ten bien kho doc (`_0x...`)
- Chuoi escape (`\x..`, `\u....`)
- Mat do ky tu dac biet cao
- Dinh dang it khoang trang de doc

`ngram_range=(1,3)` giup mo hinh hoc cac mau cuc bo nay ma khong can parser JavaScript day du.

## Vi sao can TF-IDF sau Hashing
Hashing tao khong gian dac trung lon va thua.
TF-IDF:
- Giam trong so cac token qua pho bien.
- Tang trong so token co tinh phan biet cao giua 2 lop.
- Giup mo hinh tap trung vao tin hieu quan trong hon nhieu.

## Vai tro cua RandomForest
RandomForest:
- Manh tren du lieu nhieu dac trung.
- Chiu nhieu tot nho co che ensemble.
- Giam overfitting hon mot cay quyet dinh don.
- De dung de tao baseline on dinh.

## Y nghia `class_weight="balanced"`
Du du lieu khong lech qua manh, tuy chon nay van huu ich:
- Tang chu y cho lop thieu so tuong doi.
- Giam thien lech du doan ve lop dong hon.
- Cai thien kha nang phat hien lop Obfuscated trong nhieu tinh huong.

## Gioi han can hieu dung
Pipeline hien tai:
- Chua co cross-validation.
- Chua tuning sieu tham so.
- Chua phan tich sau tap loi FP/FN.
- Chua dung dac trung ngu nghia/AST.

Nghia la: tot de lam baseline manh, nhung chua phai phien ban toi uu cuoi cung.

## Ket luan
Day la lua chon thuc dung va hieu qua cho giai doan dau:
- Trien khai nhanh.
- Hieu nang tot.
- De mo rong va cai tien theo tung vong danh gia.
