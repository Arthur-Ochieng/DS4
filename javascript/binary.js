function binary_search(list, target){
    var first = 0
    var last = list.length - 1

    while (first<=last){
        midpoint = Math.floor((first + last)/2) // Code runs into a problem because of implementation of floor division in javascript
        //console.log(midpoint)
        if (list[midpoint] == target){
            return midpoint
        }else if (midpoint > target){
            last = midpoint - 1
        }else{
            first = midpoint + 1
        }
    }
    return null
}

function verify(index){
    if (index != null){
        console.log("Target found at index: " + index);
    }else{
        console.log("Target not found in list");
    }
}

numerals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numerals, 8)
verify(result)

numerals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numerals, 5)
verify(result)