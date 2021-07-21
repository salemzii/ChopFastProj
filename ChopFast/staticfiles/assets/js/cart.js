var updateBtns = document.getElementsByClassName('update-cart')
var confirmBtns = document.getElementsByClassName('confirm-delivery')


for(i=0; i < confirmBtns.length; i++){
    confirmBtns[i].addEventListener('click', function(){
        var deliveryId = this.dataset.product
        var action = this.dataset.action
        console.log('deliveryId: ', deliveryId, 'Actions: ', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            updateDeliveryStatus(deliveryId, action)
        }
    })
}

for (i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var dishId = this.dataset.product
        var action = this.dataset.action
        console.log('dishId: ', dishId, 'Action: ', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            console.log('User is not authenticated')
        }else{
            updateUserOrder(dishId, action)
        }
    })
}

function updateDeliveryStatus(deliveryId, action){
    console.log('User is authenticated, sending data...')
    var url = '/update_delivery/'
    fetch (url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'deliveryId': deliveryId, 'action': action})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        console.log('Data: ', data)
        location.reload()
    });
}

function updateUserOrder(dishId, action){
    console.log('User is authenticated, sending data...')
    var url ='/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'dishId': dishId, 'action': action})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) => {
        console.log('Data: ', data)
        location.reload()
    });
}