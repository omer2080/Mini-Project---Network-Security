rule Ransomware_Patterns
{
    meta:
        description = "Detects patterns associated with ransomware"
        author = "OMER AND GAL"
        date = "2024-08-06"
    
    strings:
        $ransomware_note = "YOUR_FILES_HAVE_BEEN_ENCRYPTED"
        $ransomware_extension = ".encrypted"
        $ransomware_key = { 8D 45 08 6A 00 68 ?? ?? 6A 00 50 8D 4D FC 8D 55 F8 }
    
    condition:
        $ransomware_note or $ransomware_extension or $ransomware_key
}
