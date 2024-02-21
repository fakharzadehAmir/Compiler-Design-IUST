global using NUnit.Framework;
using System.Text.RegularExpressions;

public class HashtagChecking
{
    public bool IsHashtag(string input)
    {
        var pattern = new Regex(@"#(\w+)$");
        return pattern.IsMatch(input);
    }
}