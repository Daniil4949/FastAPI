import asyncio
from aio_pika import Message, connect


async def like(body) -> None:
    connection = await connect("amqp://guest:guest@rabbitmq:5672/")
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("connecting")
        await channel.default_exchange.publish(
            Message(body=body.encode()),
            routing_key=queue.name,
        )
        print(" [x] Sent info")


if __name__ == "__main__":
    asyncio.run(like("hello"))


