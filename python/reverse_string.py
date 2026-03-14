

def reverseString(string):
  # type your code here
  if len(string) <= 1:
    return string
  
  # s = string[0: len(string)-1]
  s = string[: -1]  # same as above

  return string[-1] + reverseString(s)




# if (require.main === module) {
#   # add your own tests in here
#   console.log("Expecting: 'ih'");
#   console.log("=>", reverseString('hi'));

#   console.log("");

#   console.log("Expecting: 'ybabtac'");
#   console.log("=>", reverseString('catbaby'));
# }

# module.exports = reverseString;

# Please add your pseudocode to this file
# And a written explanation of your solution
