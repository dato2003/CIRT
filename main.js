var VMs = document.getElementsByName('VM');

for (var i = 0, length = VMs.length; i < length; i++)
{
    if (VMs[i].checked)
    {
        alert(VMs[i].value);
        break;
    }
}