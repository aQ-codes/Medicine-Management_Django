const searchField = document.querySelector("#searchField");
const list = document.querySelector("#list");
const searchList = document.querySelector("#searchList");
const tbody = document.querySelector("#tbody");

searchList.style.display = 'none';





searchField.addEventListener('keyup',(e)=>{
    const searchValue = e.target.value;
    if (searchValue.trim().length > 0){
        tbody.innerHTML=''

        console.log('searchValue', searchValue)

        fetch("/search/",{
            body : JSON.stringify({searchText : searchValue}),
            method : "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("Data ",data);
            

            list.style.display = 'none';
            searchList.style.display = 'block';

            if (data.length === 0){
                searchList.innerHTML = "No Results Found"

            }

            else{
                data.forEach(item => {
                    tbody.innerHTML+=`

                    <tr>
                    <td> ${item.name} </td>
                    <td> ${item.category} </td>
                    <td> ${item.description} </td>
                    <td> ${item.price} </td>
                    <td> ${item.date_created} </td>
                    </tr>`;
                    
                });
                
            }
    
            
        });
    }

    else{
        list.style.display = 'block';
        searchList.style.display= "none";
    }

   


    
});