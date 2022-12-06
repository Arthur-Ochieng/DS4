function IsSorted(list){
    n = list.length
    for(i=0; i<n-1; i++){
        if(list[i] > list[i + 1])
        {
            return false
        }
    } return true
}

function bogoSort(arr) {
    var count = 0
    while(!IsSorted(arr)){
        arr.sort(() => Math.random() - 0.5);
        count += 1
    }
    return [arr, count]
}

let arr = [13, 52, 33, 27, 68];
var b = bogoSort(arr);
console.log(b)

