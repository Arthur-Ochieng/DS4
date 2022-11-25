function linear_search(list, target){
    for (var i = 0; i < list.length; i++){
        if (list[i] == target){
            return i;
        }
    }
    return null;
}

function verify(index){
    if (index != null){
        console.log("Target found at index: " + index);
    }else{
        console.log("Target not found in list");
    }
}

numerals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numerals, 8)

verify(result)