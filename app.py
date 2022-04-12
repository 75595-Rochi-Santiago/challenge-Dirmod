
def encode(n,ct):
       s=""
       if n!=0:
              n+=1
       for i in range(ct):
              s+=str(n)
       return s

def inputValidate(text):
       str_list=text.split()
       for st in str_list:
              if st.isalpha()==False:
                     return False
       return True


def calculeSequence(msg):
       pool=[
       [" "],
       ["A","B","C"],
       ["D","E","F"],
       ["G","H","I"],
       ["J","K","L"],
       ["M","N","O"],
       ["P","Q","R","S"],
       ["T","U","V"],
       ["W","X","Y","Z"]
       ]

       if inputValidate(msg):
              text=msg.upper()
              res=""
              aux=0
              for char in text:
                     for num in range( len(pool) ):
                            ct=0
                            for cn in pool[num]:
                                   ct+=1
                                   if char==cn:
                                          if aux==num:
                                                 res+=" "
                                          aux=num
                                          res+=encode(num, ct)
              return res
       else:
              return "Invalid Input"

def main():
       print("Enter message:")
       msg=str(input(">"))
       res=calculeSequence(msg)
       print(res)

main()