namespace Assignment1.Tests
{
    public class Question1
    {
        [Test]
        public void UrlTest()
        {
            var checkFunction = new UrlChecker();
            Assert.Multiple(() =>
            {
                Assert.That(checkFunction.ValidateUrl("invalid-url"), Is.False);
                Assert.That(checkFunction.ValidateUrl("http://example.com/invalid-"), Is.False);
                Assert.That(checkFunction.ValidateUrl("example.com"), Is.False);
                Assert.That(checkFunction.ValidateUrl("ftp://ftp.example.com"), Is.True);
                Assert.That(checkFunction.ValidateUrl("https://www.example.com"), Is.True);
            });
        }
    }
}