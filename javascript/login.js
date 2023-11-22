const users= [
    {id: 1, email: 'admin@email.com', password: 'admin', role:'admin'},
    {id: 2, email: 'xayme@email.com', password: '1337', role: 'user'},
    {id: 3, email: 'xapasa@email.com', password: '1171', role:'user'},
]
function login(){
    const email = document.getElementById('email').value
    const password = document.getElementById('password').value
    console.log({email,password})
    // use array method
    // check user
    // if user role is admin, redirect to admin page [admin.html]
    // if user role is user, redirect to user page [user.html]

}


