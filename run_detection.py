import os
from sklearn.feature_extraction.text import HashingVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score
from sklearn.pipeline import Pipeline
import time
js_path = "./JavascriptSamples"
obfuscated_js_path = "./JavascriptSamplesObfuscated"

corpus = []
labels = []
a = time.time()

file_types_and_labels = [(js_path, 0), (obfuscated_js_path, 1)]

for files_path, label in file_types_and_labels:
    files = os.listdir(files_path)
    for file in files:
        file_path = files_path + "/" + file
        try:
            with open(file_path, "r") as myfile:
                data = myfile.read().replace("\n", "")
                data = str(data)
                corpus.append(data)
                labels.append(label)
        except:
            pass

X_train, X_test, y_train, y_test = train_test_split(
    corpus, labels, test_size=0.33, random_state=42
)
text_clf = Pipeline(
    [
        ("vect", HashingVectorizer(input="content", ngram_range=(1, 3))),
        ("tfidf", TfidfTransformer(use_idf=True,)),
        ("rf", RandomForestClassifier(class_weight="balanced")),
    ]
)
text_clf.fit(X_train, y_train)

y_test_pred = text_clf.predict(X_test)

# Tính các tỷ lệ đánh giá
print("\n=== KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH ===\n")

# 1. Accuracy (Độ chính xác tổng thể)
acc = accuracy_score(y_test, y_test_pred)
print(f"Accuracy: {acc:.4f} ({acc*100:.2f}%)")

# 2. Confusion Matrix
cm = confusion_matrix(y_test, y_test_pred)
print(f"\nConfusion Matrix:")
print(f"                 Predicted")
print(f"                 Normal  Obfuscated")
print(f"Actual Normal      {cm[0][0]:4d}     {cm[0][1]:4d}")
print(f"       Obfuscated  {cm[1][0]:4d}     {cm[1][1]:4d}")

# Tính TP, TN, FP, FN
TN, FP = cm[0][0], cm[0][1]
FN, TP = cm[1][0], cm[1][1]
print(f"\nTP (True Positive - Phát hiện đúng obfuscated): {TP}")
print(f"TN (True Negative - Phát hiện đúng normal): {TN}")
print(f"FP (False Positive - Nhầm normal thành obfuscated): {FP}")
print(f"FN (False Negative - Bỏ sót obfuscated): {FN}")

# 3. Precision (Độ chính xác khi dự đoán obfuscated)
precision = precision_score(y_test, y_test_pred)
print(f"\nPrecision: {precision:.4f} ({precision*100:.2f}%)")
print(f"  → Trong số các file được dự đoán là obfuscated, {precision*100:.2f}% thực sự là obfuscated")

# 4. Recall/Sensitivity (Độ nhạy - khả năng phát hiện obfuscated)
recall = recall_score(y_test, y_test_pred)
print(f"\nRecall (Sensitivity): {recall:.4f} ({recall*100:.2f}%)")
print(f"  → Phát hiện được {recall*100:.2f}% các file obfuscated thực tế")

# 5. Specificity (Độ đặc hiệu - khả năng phát hiện normal)
specificity = TN / (TN + FP) if (TN + FP) > 0 else 0
print(f"\nSpecificity: {specificity:.4f} ({specificity*100:.2f}%)")
print(f"  → Phát hiện đúng {specificity*100:.2f}% các file normal thực tế")

# 6. F1-Score (Trung bình điều hòa của Precision và Recall)
f1 = f1_score(y_test, y_test_pred)
print(f"\nF1-Score: {f1:.4f}")
print(f"  → Cân bằng giữa Precision và Recall")

# 7. Classification Report (Báo cáo chi tiết)
print(f"\n=== CLASSIFICATION REPORT ===\n")
print(classification_report(y_test, y_test_pred, 
                          target_names=['Normal JS', 'Obfuscated JS'],
                          digits=4))
print(time.time()-a)
