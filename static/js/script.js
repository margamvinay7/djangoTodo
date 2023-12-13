const inputfield=document.querySelector('#input')
const formmethod=document.querySelector('form')
inputfield.focus()
const updatetodo=async (todo,id)=>{
    inputfield.focus()
    inputfield.value=todo
    
      inputfield.addEventListener('change',(e)=>{
        // e.preventDefault()
        inputfield.value=e.target.value
        
        
     
    })
    
    formmethod.action=`updatetodo/${id}`
    //formmethod.submit() // if use this directly submitted not wait until changed
    
    
   
    
}

