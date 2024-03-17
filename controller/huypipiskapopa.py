from disnake.ext import commands
from view.console_out import log, important, warning, error


class Huy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        important("COGS module Huy connected")

    @commands.command(
        name="Huy",
        usage="/sosnul_huica",
        description="Соснуть хуйца 10 раз"
    )
    async def sosnul_huica(self, ctx):
        log(f"{ctx.author} used /sosnul_huica")
        a = 3
        while a != 0:
            await ctx.send(f'{ctx.author.mention} *сосет*')
            a -= 1


def setup(bot):
    bot.add_cog(Huy(bot))