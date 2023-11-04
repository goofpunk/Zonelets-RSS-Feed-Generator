# Zonelets-RSS-Feed-Generator
**UPDATE: This project is no longer actively being maintained, since I'm no longer using Zonelets. It *should* still work, but I can't guarantee it. If you're using it and you run into a problem, submit an issue and I'll see what I can do.** 

[Zonelets](https://zonelets.net/index.html) is an awesome, easy way to generate a blog on a simple hosting platform like Neocities. I highly recommend it for anyone looking for a simple blogging tool.

One feature it’s missing, though, is the ability to generate an [RSS feed](https://en.wikipedia.org/wiki/RSS) for your blog. I’m a big user of RSS, and I want to have one for my blog too. And since RSS is just based on a hosted XML file, and there’s a standard format for file names in Zonelets, I figured there’s no reason you couldn’t write a script that would generate that XML file based on your list of posts in Zonelets’s `script.js` file. So I made one! 

Before you go and use it yourself, though, know that it’s not entirely feature-complete right now. All it does is generate an entry in the feed with your post title, and a link to the page, it can’t display the content of your posts in an RSS reader, but that’s a feature I plan on adding. It’s also *very* strict on your formatting in the `script.js` file. If you don’t follow it exactly, your titles will be wrong. That’s not something I plan on changing right now, because accounting for all the various ways people could format their strings would be a hassle. Also, the code is extremely messy, because I haven’t gone back to clean it up yet.

If you’re fine with all that, and you want to try it out, go ahead and download the Python file from my GitHub, place it in the main directory of your blog (/blog/ on this site, but if your site is *just* a Zonelets site, it would be the root directory), and then run the script with Python 3. It will spit out a file called `rss.xml`, and then you can just upload your site to Neocities like normal. Your feed will be hosted at `YOURBLOGSURL/rss.xml`.

Let me know if you’re using it! If you don’t want to use it yourself yet, but you still want to see how it goes, go ahead and follow my blog using [this link](https://goofpunk.com/blog/rss.xml). Either way, let me know if you run into any bugs or other issues, so I can iron them out and get a proper release ready.
