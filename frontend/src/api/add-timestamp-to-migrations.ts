import { Client } from 'pg';

const client = new Client({
  connectionString: 'postgresql://race_management_db_user:ZjMr4YppbEE0shbkM9XLMmOn8QJQQr3g@dpg-d384efgdl3ps73avnjf0-a.frankfurt-postgres.render.com:5432/race_management_db?sslmode=require',
});

async function addTimestampColumn() {
  try {
    await client.connect();
    await client.query('ALTER TABLE migrations ADD COLUMN "timestamp" BIGINT;');
    console.log('timestamp column added to migrations table.');
  } catch (err) {
    console.error('Error adding timestamp column:', err);
  } finally {
    await client.end();
  }
}

addTimestampColumn();
