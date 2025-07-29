# Widget Canvas Builder

A comprehensive widget canvas builder application with AI integrations, real-time collaboration, and advanced canvas management capabilities.

## Features

- **User Authentication**: WorkOS integration for secure authentication
- **Canvas Management**: Create, edit, and share interactive canvases
- **Widget System**: Drag-and-drop widgets with customizable properties
- **AI Integrations**: 
  - OpenAI DALL-E for image generation
  - Google Gemini for text generation
  - Google Veo for video generation (placeholder)
- **Real-time Collaboration**: WebSocket-based MCP server for live updates
- **Database**: PostgreSQL with SQLAlchemy ORM
- **API**: FastAPI with comprehensive REST endpoints

## Architecture

### Database Models
- **User**: User accounts with WorkOS integration
- **Canvas**: Interactive canvases with widgets
- **Widget**: Draggable elements with properties and styling
- **AIGeneration**: Track AI-generated content
- **Session**: User session management

### API Endpoints
- **/auth**: Authentication and session management
- **/users**: User profile management
- **/canvases**: Canvas CRUD operations
- **/widgets**: Widget management
- **/ai**: AI generation services

### MCP Server
WebSocket-based Model Context Protocol server for:
- Real-time canvas updates
- AI generation requests
- Live collaboration features

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`
4. Initialize database: `alembic upgrade head`
5. Run the application: `uvicorn app.main:app --reload`
6. Start MCP server: `python -m app.mcp.server`

## Environment Variables

```
DATABASE_URL=postgresql://user:password@localhost/widget_canvas
WORKOS_API_KEY=your_workos_api_key
WORKOS_CLIENT_ID=your_workos_client_id
JWT_SECRET_KEY=your_jwt_secret
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
REDIS_URL=redis://localhost:6379
```

## Usage

### Creating a Canvas
```python
POST /canvases/
{
    "title": "My Canvas",
    "description": "A sample canvas",
    "width": 1920,
    "height": 1080
}
```

### Adding Widgets
```python
POST /widgets/
{
    "canvas_id": "canvas-uuid",
    "type": "text",
    "content": "Hello World",
    "x_position": 100,
    "y_position": 100
}
```

### AI Generation
```python
POST /ai/generate/image
{
    "prompt": "A beautiful landscape",
    "model": "dall-e-3",
    "size": "1024x1024"
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License
