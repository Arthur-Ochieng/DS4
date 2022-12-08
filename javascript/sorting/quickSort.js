alist = [11,2,44,15,6,9,77]

function swap(list, leftIndex, rightIndex){
    var temp = list[leftIndex];
    list[leftIndex] = list[rightIndex]
    list[rightIndex]= temp 
}

function partition(list,left, right){
    pivot = list[Math.floor((right + left) / 2)] //Middle element
    leftPointer = left
    rightPointer = right
    // console.log([pivot, leftPointer, rightPointer])
    while (leftPointer <= rightPointer){
        while (list[leftPointer] < pivot){
            leftPointer ++
            // console.log(leftPointer)
        }
        while (list[rightPointer] > pivot){
            rightPointer --
            // console.log(rightPointer)
        }
        if (leftPointer <= rightPointer){
            swap(list, leftPointer, rightPointer)
            leftPointer ++;
            rightPointer --;
        }
    }
    return leftPointer;
}

function quicksort(list, left, right){
    var index;
    if(list.length > 1){
        index = partition(list, left, right); // Index returned form perfroming the partition
        if(left < index - 1){
            quicksort(list, left, index -1); // Means that there are more elements on the left side of the array
        }
        if(index < right){
            quicksort(list, index, right);  // More elements on the right side of the pivot
        }
    }
    return list;
}

console.log(quicksort(alist, 0, alist.length -1))