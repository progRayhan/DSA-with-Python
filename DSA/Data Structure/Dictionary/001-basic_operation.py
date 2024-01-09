# dictionary is mutable
exam_result = {
    "bengali": 75,
    "english": 80,
    "islam": 90
}

exam_result["bengali"] = 82 # mutable
print(exam_result)

# delete item from dictionary
del exam_result["bengali"]
print(exam_result)
