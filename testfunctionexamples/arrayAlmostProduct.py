def function(arr):
    if len(arr) == 1:
        return None;
    newArr = [1] * len(arr);
    i = len(newArr) - 2;
    while (i > -1):
        newArr[i] = newArr[i+1] * arr[i+1];
        i = i - 1;
    newArr[len(newArr)-1] = arr[1];
    arr[1] = arr[0];
    arr[0] = newArr[len(newArr)-1];
    for i in range (2,len(arr)):
        newArr[len(newArr)-1] = arr[i];
        arr[i] = arr[i-1]*arr[0];
        arr[0] = newArr[len(newArr)-1];
    arr[0] = 1;
    newArr[len(newArr)-1] = 1;
    for i in range (len(newArr)):
        newArr[i] = newArr[i]*arr[i];
    return newArr;
