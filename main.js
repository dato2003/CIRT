function GetInput() {
    var VMs = document.getElementsByName('Option');
    
    for (var i = 0, length = VMs.length; i < length; i++)
    {
        if (VMs[i].checked)
        {
            sessionStorage.setItem("Choice",VMs[i].value);
            alert(VMs[i].value);
            document.location.href = "checkout.html";
            break;
        }
    }   
}