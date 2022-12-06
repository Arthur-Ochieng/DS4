function recursive_binary_search(list, target){
    if (list.length == 0){
        return false
    }
    else{
        var midpoint = Math.floor((list.length)/2)
        if (list[midpoint] == target){
            return true
        }
        else if (list[midpoint] < target){
            return recursive_binary_search(list.slice(midpoint+1,list.length), target)
        }
        else{
            return recursive_binary_search(list.slice(0,midpoint),target)
        }
    }
}

function verify(result){
    console.log("Target found: ", result)
}

var numbers = [1,2,3,4,5,6,7,8]
var target = 7
result = recursive_binary_search(numbers, target)
verify(result)

var numbers = [1,2,3,4,5,6,7,8]
var target = 13
result = recursive_binary_search(numbers, target)
verify(result)
