# Reference: `run_detection.py`

Tai lieu nay mo ta ky thuat cua script, khong huong dan tung buoc.

## Muc dich
Huan luyen va danh gia mo hinh phan loai JavaScript thuong vs JavaScript obfuscated.

## Input du lieu
- Thu muc normal: `./JavascriptSamples`
- Thu muc obfuscated: `./JavascriptSamplesObfuscated`
- Moi file duoc doc toan bo noi dung thanh chuoi.

## Nhan lop
- `0`: Normal JS
- `1`: Obfuscated JS

## Pipeline xu ly
1. `HashingVectorizer(input="content", ngram_range=(1, 3))`
2. `TfidfTransformer(use_idf=True)`
3. `RandomForestClassifier(class_weight="balanced")`

## Chia du lieu
- Ham: `train_test_split(corpus, labels, test_size=0.33, random_state=42)`

## Chi so in ra
- `accuracy_score`
- `confusion_matrix`
- `precision_score`
- `recall_score`
- `f1_score`
- `classification_report`
- `specificity` (tu tinh tu confusion matrix)

## Output
In ra terminal:
- Accuracy phan tram
- Confusion matrix dang bang
- TP/TN/FP/FN
- Precision/Recall/Specificity/F1
- Classification report chi tiet

## Hanh vi loi du lieu
- Khi doc file loi, script `except: pass` va bo qua file do.

## Do phuc tap thuc te
- Thoi gian chay phu thuoc so luong file va cau hinh may.
- Du lieu van ban lon co the tang thoi gian vector hoa + huan luyen.
