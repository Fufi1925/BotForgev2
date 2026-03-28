from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get("/features")
async def features() -> dict[str, list[str]]:
    return {
        "moderation": ["ki_spam_schutz", "ghost_ping", "zalgo_killer", "invite_blocker"],
        "antiraid": ["join_gate", "mass_join_sperre", "vpn_detection"],
        "music": ["lavalink", "spotify", "audio_filter", "24_7_mode"],
        "tracking": ["voice_logger", "heatmaps", "word_cloud"],
    }
