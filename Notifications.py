import asyncio
from EmbedCreator import EmbedCreator
from Constants import Constants
from Database import Database
import time
import hikari

class Notifications:
    async def OFNotification(rest: hikari.impl.RESTClientImpl, title, largeThumbnail, icon):
        embedMaker = EmbedCreator(
                                    Constants.streamerName + " is now live on Onlyfans!", 
                                    title, 
                                    Constants.OfLiveStreamUrl, 
                                    'images/platformImages/OFImage.png', 
                                    Constants.ofEmbedColor, 
                                    icon, 
                                    Constants.ofUserName
                                )
        task = asyncio.create_task(embedMaker.getEmbed())
        ofEmbed = await task
        db = Database()
        db.updateTableRowCol("platforms","onlyfans","last_online_message",time.time())
        PING_EVERYONE = db.getPing()
        messageContent = "@everyone " + Constants.ofOnlineText if PING_EVERYONE else Constants.ofOnlineText
        await rest.create_message(channel = Constants.STDOUT_CHANNEL_ID, content = messageContent, embed = ofEmbed, mentions_everyone= PING_EVERYONE)

    async def ChaturNotification(rest: hikari.impl.RESTClientImpl, title, largeThumbnail, icon):
        embedMaker = EmbedCreator(
                                    f"{Constants.streamerName} is now live on Chaturbate!", 
                                    title, 
                                    Constants.cbLiveStreamUrl, 
                                    'images/platformImages/CbImage.png', 
                                    Constants.cbEmbedColor, 
                                    icon, 
                                    Constants.cbUserName, 
                                    largeThumbnail= largeThumbnail, 
                                    useTwitter=False
                                )
        task = asyncio.create_task(embedMaker.getEmbed())
        cbEmbed = await task
        db = Database()
        db.updateTableRowCol("platforms","chaturbate","last_online_message",time.time())
        PING_EVERYONE = db.getPing()
        messageContent = "@everyone " + Constants.cbOnlineText if PING_EVERYONE else Constants.cbOnlineText
        await rest.create_message(channel = Constants.STDOUT_CHANNEL_ID, content = messageContent, embed=cbEmbed, mentions_everyone= PING_EVERYONE)

    async def FansNotification(rest: hikari.impl.RESTClientImpl, title, largeThumbnail, icon):
        embedMaker = EmbedCreator(
                                    Constants.streamerName + " is now live on Fansly!", 
                                    title, 
                                    Constants.fansLiveStreamUrl, 
                                    'images/platformImages/FansImage.png', 
                                    Constants.fansEmbedColor, 
                                    icon, 
                                    Constants.fansUserName
                                )
        task = asyncio.create_task(embedMaker.getEmbed())
        fansEmbed = await task
        db = Database()
        db.updateTableRowCol("platforms","fansly","last_online_message",time.time())
        PING_EVERYONE = db.getPing()
        messageContent = "@everyone " + Constants.fansOnlineText if PING_EVERYONE else Constants.fansOnlineText
        await rest.create_message(channel = Constants.STDOUT_CHANNEL_ID, content = messageContent, embed = fansEmbed, mentions_everyone=PING_EVERYONE)

    async def TwitchNotification(rest: hikari.impl.RESTClientImpl, title, largeThumbnail, icon):
        embedMaker = EmbedCreator(
                                    Constants.streamerName + " is now live on Twitch!", 
                                    title, 
                                    Constants.twitchUrl, 
                                    'images/platformImages/twitchImage.png', 
                                    Constants.twitchEmbedColor, 
                                    icon, 
                                    Constants.twitchUserName, 
                                    largeThumbnail= largeThumbnail
                                )
        task = asyncio.create_task(embedMaker.getEmbed())
        twitchEmbed = await task
        db = Database()
        db.updateTableRowCol("platforms","twitch","last_online_message",time.time())
        PING_EVERYONE = db.getPing()
        messageContent = "@everyone " + Constants.twitchOnlineText if PING_EVERYONE else Constants.twitchOnlineText
        await rest.create_message(channel = Constants.STDOUT_CHANNEL_ID, content = messageContent, embed=twitchEmbed, mentions_everyone= PING_EVERYONE)
    
    async def YTNotification(rest: hikari.impl.RESTClientImpl, title, largeThumbnail, icon):
        embedMaker = EmbedCreator(
                                    Constants.streamerName + " is now live on YouTube!", 
                                    title, 
                                    Constants.ytUrl, 
                                    'images/platformImages/ytImage.png', 
                                    Constants.ytEmbedColor, 
                                    icon, 
                                    Constants.ytUserName, 
                                    largeThumbnail= largeThumbnail
                                )
        task = asyncio.create_task(embedMaker.getEmbed())
        ytEmbed = await task
        db = Database()
        db.updateTableRowCol("platforms","youtube","last_online_message",time.time())
        PING_EVERYONE = db.getPing()
        messageContent = "@everyone " + Constants.ytOnlineText if PING_EVERYONE else Constants.ytOnlineText
        await rest.create_message(channel = Constants.STDOUT_CHANNEL_ID, content = messageContent, embed=ytEmbed, mentions_everyone= PING_EVERYONE)
    
    async def KickNotification(rest: hikari.impl.RESTClientImpl, title, largeThumbnail, icon):
        embedMaker = EmbedCreator(
                                    Constants.streamerName + " is now live on Kick!", 
                                    title, 
                                    Constants.kickUrl, 
                                    'images/platformImages/KickImage.png', 
                                    Constants.kickEmbedColor, 
                                    icon, 
                                    Constants.kickUserName, 
                                    largeThumbnail= largeThumbnail
                                )
        task = asyncio.create_task(embedMaker.getEmbed())
        kickEmbed = await task
        db = Database()
        db.updateTableRowCol("platforms","kick","last_online_message",time.time())
        PING_EVERYONE = db.getPing()
        messageContent = "@everyone " + Constants.kickOnlineText if PING_EVERYONE else Constants.kickOnlineText
        await rest.create_message(channel = Constants.STDOUT_CHANNEL_ID, content = messageContent, embed=kickEmbed, mentions_everyone= PING_EVERYONE)

    async def Cam4Notification(rest: hikari.impl.RESTClientImpl, title, largeThumbnail, icon):
        embedMaker = EmbedCreator(
                                    Constants.streamerName + " is now live on Cam4!", 
                                    title, 
                                    Constants.cam4Url, 
                                    'images/platformImages/cam4Image.png', 
                                    Constants.cam4EmbedColor, 
                                    icon, 
                                    Constants.cam4UserName, 
                                    largeThumbnail= largeThumbnail
                                )
        task = asyncio.create_task(embedMaker.getEmbed())
        cam4Embed = await task
        db = Database()
        db.updateTableRowCol("platforms","cam4","last_online_message",time.time())
        PING_EVERYONE = db.getPing()
        messageContent = "@everyone " + Constants.cam4OnlineText if PING_EVERYONE else Constants.cam4OnlineText
        await rest.create_message(channel = Constants.STDOUT_CHANNEL_ID, content = messageContent, embed=cam4Embed, mentions_everyone= PING_EVERYONE)