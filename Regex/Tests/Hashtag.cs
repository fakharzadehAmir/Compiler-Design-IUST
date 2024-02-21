namespace Assignment1.Tests;

public class Question3
{
    [Test]
    public void HashtagTest()
    {
        var checkFunction = new HashtagChecking();
        Assert.Multiple(() =>
        {
            Assert.That(checkFunction.IsHashtag("#amir"), Is.True);
            Assert.That(checkFunction.IsHashtag("#amir-fakharzadeh"), Is.False);
            Assert.That(checkFunction.IsHashtag("#amir99521487"), Is.True);
            Assert.That(checkFunction.IsHashtag("amir"), Is.False);
            Assert.That(checkFunction.IsHashtag("#amir_Fakharzadeh"), Is.True);
            Assert.That(checkFunction.IsHashtag("#_amir+"), Is.False);
        });
    }
}