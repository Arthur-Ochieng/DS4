function selectionSort(arr){
    sortedList = []
    for(i=0; i<arr.length; i++){
        movingIndex = indexMin(arr)
        sortedList.push(arr[movingIndex])
        arr.pop(movingIndex)

        console.log("poped array",arr)
        console.log(sortedList)
    }
    return sortedList
}

function indexMin(arr){
    let minIndex = 0
    for(i=1; i<arr.length; i++){
        if(arr[i] < arr[minIndex]){
            minIndex = i
        }
    } 
    return minIndex
}

arr = [11,2,44,15,6,9,7]
verify = selectionSort(arr)
// console.log(verify)

// for (i=0; i<5; i++){
//     console.log("this is the number", i)
// }