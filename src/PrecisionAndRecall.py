# ví dụ về độ chính xác và thu hồi
'''
    pred/outcome        pos     neg
        pos             1       0
                        tp      fn
        neg             2       1
                        fp      tn
    lấy n là kích thước của tập dữ liệu
    tp và fp là đúng và sai tích cực tương ứng
    tn và fn là đúng và sai tiêu cực tương ứng
    Accuracy (độ chính xác) là tỷ lệ % của câu trả lời đúng trên tổng số dữ liệu (tp + tn) / n
    Precision (chính xác) là tỷ lệ % của tích cực đúng trong các dự đoán tích cực tp / (tp + fp)
    Recall (thu hồi) là tỷ lệ của tích cực đúng trong tích cực thực tế tp / (tp + fn)
'''


def do_evaluation(pairs, pos_cls='pos'):
    (N, tp, tn, fp, fn) = (0, 0, 0, 0, 0)
    for (predicted, actual) in pairs:
        N += 1
        if predicted == actual:
            if actual == pos_cls:
                tp += 1
            else:
                tn += 1
        else:
            if actual == pos_cls:
                fn += 1
            else:
                fp += 1
        pass
    pass
    accuracy = float((tp + tn) / N)
    print('accuracy = (', tp, '+', tn, ') / ', N)
    precision = float(tp / (tp + fp))
    print('precision = ', tp, ' / (', tp, ' + ', fp, ')')
    recall = float(tp / (tp + fn))
    print('recall = ', tp, ' / (', tp, ' + ', fn, ')')
    return (accuracy, precision, recall)


pass

data = [('sunny', 'sunny'), ('sunny', 'cloudy'), ('sunny', 'rainy'), ('rainy', 'rainy')]
(acc, pre, rec) = do_evaluation(data, pos_cls='sunny')
print('acc = {0:.2f}, pre = {1:.2f}, rec = {2:.2f}'.format(acc, pre, rec))
